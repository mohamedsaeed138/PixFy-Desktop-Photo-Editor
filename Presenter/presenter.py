from enum import Enum
from os import getcwd
from PIL.ImageTk import PhotoImage
from customtkinter import filedialog, END, CTkEntry, CTkSwitch
from tkinter import Event, IntVar, messagebox
from Model.image_Model import ImageModel
from os.path import splitext
from .choice_enums import GrayTabChoice, NoiseChoice, SharpeningChoice,SmoothingChoice,EdgeDetectionChoice
from re import match

#from Views.Main_Screen.main_screen import MainScreen


class ValidationResult(Enum):
    Empty = -1
    NotValid = 0
    Valid = 1


class Presenter:
    def __init__(self, model: ImageModel, view):
        self.model = model
        self.view = view
        self.gray_tab_effects_dict={GrayTabChoice.Threshold.value:self.model.threshold,
                            GrayTabChoice.Negative.value:self.model.negative,
                            GrayTabChoice.Stretching.value:self.model.contrast_stretching,
                            GrayTabChoice.Equalization.value:self.model.equalization,
                            GrayTabChoice.LogTransform.value:self.model.log_transform,
                            GrayTabChoice.PowerLaw.value:self.model.power_law}
        self.smoothing_tab_effects_dict={
            SmoothingChoice.Gaussian.value:self.model.smooth_gaussian_filter,
            SmoothingChoice.Box.value:self.model.smooth_box_filter,
            SmoothingChoice.Mean.value:self.model.smooth_mean_filter,
            SmoothingChoice.Median.value:self.model.smooth_median_filter,
            SmoothingChoice.Max.value:self.model.smooth_max_filter,
            SmoothingChoice.Min.value:self.model.smooth_min_filter
        }
        self.edge_tab_effects_dict={
            EdgeDetectionChoice.Canny.value:self.model.canny_detection,
            EdgeDetectionChoice.SobelXY.value:self.model.sobelxy_detection,
            EdgeDetectionChoice.SobelX.value:self.model.sobelx_detection,
            EdgeDetectionChoice.SobelY.value:self.model.sobely_detection,
        }
        self.events = []
        self.gray_match = lambda event: event == self.model.gray_scale_filter
        self.rotate_match = lambda event: event == self.model.rotate
        self.view_size = tuple[int, int]

    # region manage events list
    def remove_event(self, match):
        self.events = [event for event in self.events if not match(event[0])]

    def add_or_update_event(self, event, match):
        self.remove_event(match=match)
        self.events.append(event)

    # endregion
    #region save image
    def save_image(self):
        if self.model.image is None:
            messagebox.showinfo('info','select or drop an image first.')
            return
        path = filedialog.asksaveasfilename(defaultextension=".png",
                                               filetypes=[("JPEG files", "*.jpg"),
                                                           ("PNG files", "*.png"), 
                                                           ("All files", "*.*")])
        if not path: return
        _,format=splitext(path)
        format=format.lower()
        image =self.model.edited_image.convert("RGB") if format=='.jpg' else self.model.edited_image
        image.save(path)
        messagebox.showinfo('info','Image is saved successfully !')
    #endregion
    # region select new image
    def drop_image(self, event: Event):
        path: str = event.data.strip(r"{}")
        try:
            is_no_image_yet=self.model.image is None
            self.model.set_images(path)
            self.update_view_image_containers(
                max_size=self.view.original_image_container.label_size()
            )
            self.events=[]
            if is_no_image_yet :
                self.view.editor_menu.enable()
            else:
                self.view.rebuild_editor_menu()
        except:
            messagebox.showerror("error", "This Format isn't supported !")

    def upload_image(self):
        path = filedialog.askopenfilename(
            initialdir=getcwd(),
            title="Select Image",
            filetypes=(("Image files", "*.png;*.jpg;*.jpeg"),),
        )
        if path == "":
            return
        try:
            is_no_image_yet=self.model.image is None
            self.model.set_images(path)
            self.update_view_image_containers(
                max_size=self.view.original_image_container.label_size()
            )
            self.events=[]
            if is_no_image_yet:
                self.view.editor_menu.enable()
            else:
                self.view.rebuild_editor_menu()
            
        except:
            messagebox.showerror("error", "This Format isn't supported !")

    # endregion
    # region rescale view images (resizing window)
    def rescale_images(self, event):
        if self.model.image is None:
            return
        self.update_view_image_containers((event.width, event.height))
    # endregion
    # region update view images
    def update_view_image_containers(self, max_size: tuple[int, int]):
        original_scaled, edited_scaled = self.model.get_scaled_images(max_size)
        original_photo, edited_photo = PhotoImage(original_scaled), PhotoImage(
            edited_scaled
        )
        
        self.view.original_image_container.image_label.configure(image=original_photo)
        self.view.edited_image_container.image_label.configure(image=edited_photo)
        # self.view.original_image_container.image_label._image = original_photo
        # self.view.edited_image_container.image_label._image = edited_photo

        original_size, edited_size = self.model.image.size, self.model.edited_image.size
        original_ratio = original_size[0] / original_scaled.size[0]
        edited_ratio = edited_size[0] / edited_scaled.size[0]
        self.view.original_image_container.size_label().configure(
            text=self.format_size_ratio(original_size,original_ratio)
        )
        self.view.edited_image_container.size_label.configure(
          text=self.format_size_ratio(edited_size,edited_ratio)
        )

    def format_size_ratio(self, size: tuple[int, int], ratio: float):
        return f"{size[0]} x {size[1]}    ratio= {f"{round(ratio,4)} : 1" if ratio > 1 else f"1 : {round(1/ratio,4)}"}"

    # def format_ratio(self, ratio: float) -> str:
    #     return f"{round(ratio,4)} : 1" if ratio > 1 else f"1 : {round(1/ratio,4)}"

    # def format_size(self, size: tuple[int, int]) -> str:
    #     return f"{size[0]}x{size[1]}"

    # endregion
    # region update view edited
    def update_view_edited_container(self):
        edited_size = self.model.edited_image.size
        max_size = self.view.original_image_container.label_size()
        edited_image = self.model.get_scaled_edited_image(max_size)
        ratio = edited_size[0] / edited_image.size[0]
        edited_photo = PhotoImage(edited_image)
        self.view.edited_image_container.image_label.configure(image=edited_photo)
        self.view.edited_image_container.image_label._image = edited_photo
        self.view.edited_image_container.size_label.configure(
             text=self.format_size_ratio(edited_size,ratio)
        )

    # endregion

    # region manage user  edits
    def histogram_handler(self):
        if self.view.editor_menu.gray_filters_tab.gray_switch.get() == 0:
            messagebox.showinfo("Note", "Enable Gray Scale Filter first !")
            return
        self.model.histogram()
    def rotate_handler(self, event):
        angle_entry: CTkEntry = self.view.editor_menu.transform_tab.rotate_angle_entry
        self.validate_entry(
            entry=angle_entry,
            regex=r"^[+-]?(?!0+$)0*\d+$",
            error_message="Enter an int value !",
            event=self.model.rotate,
            event_match=lambda event: event == self.model.rotate,
        )
    def gray_handler(self):
        switch:CTkSwitch=self.view.editor_menu.gray_filters_tab.gray_switch
        tabs=self.view.editor_menu
        is_any_dependent_on= not (tabs.noise_tab.selected_var.get()==-1
                             and tabs.edge_detection_tab.selected_var.get()==-1
                             and tabs.gray_filters_tab.selected_var.get()==-1)
        
        if switch.get() == 1:
            self.add_or_update_event(
                event=(self.model.gray_scale_filter, (None)),
                match=lambda event:event==self.model.gray_scale_filter,
            )
        elif is_any_dependent_on:
            switch.select()
            messagebox.showinfo("info", "Disable all Gray Scale Filter Dependents first !")
            return
        else:
            self.remove_event(match=lambda event:event==self.model.gray_scale_filter)
        self.model.apply_edits(self.events)
        self.update_view_edited_container()

    def resize_handler(self, current_is_width:bool):
        current_entry=self.view.editor_menu.transform_tab.resize_width_entry
        another_entry=self.view.editor_menu.transform_tab.resize_height_entry
        if not current_is_width:
            current_entry,another_entry=(another_entry,current_entry)
  
        self.validate_coupled_entries(current_entry=current_entry,
                              another_entry=another_entry,
                              regex=r'^(?!0+$)0*\d+$',
                              reversed=not current_is_width,
                              error_message='Enter a positive int value !',
                              event=self.model.resize,
                              event_match=lambda event:event==self.model.resize)
        
    def translate_handler(self, current_is_x:bool):
        current_entry=self.view.editor_menu.transform_tab.translate_x_entry
        another_entry=self.view.editor_menu.transform_tab.translate_y_entry
        if not current_is_x:
            current_entry,another_entry=(another_entry,current_entry)
        
        self.validate_uncoupled_entries(current_entry=current_entry,
                              another_entry=another_entry,
                              regex=r"^[+-]?(?!0+$)0*\d+$",
                              reversed=not current_is_x,
                              error_message='Enter a positive int value !',
                              event=self.model.translate,
                              event_match=lambda event:event==self.model.translate)
    def threshold_handler(self,event):
        threshold_entry: CTkEntry=self.view.editor_menu.gray_filters_tab.threshold_entry
        self.validate_entry(
            entry=threshold_entry,
            regex=r"^[+]?0*\d+$",
            error_message="Enter an int value !",
            event=self.model.threshold,
            event_match=lambda event: event == self.model.threshold,
        )
    def gray_radio_handler(self):
        threshold_entry:CTkEntry=self.view.editor_menu.gray_filters_tab.threshold_entry
        old= self.view.editor_menu.gray_filters_tab.was_selected
        selected_var:IntVar=self.view.editor_menu.gray_filters_tab.selected_var
        
        if self.view.editor_menu.gray_filters_tab.gray_switch.get() == 0:
            messagebox.showinfo("info", "Enable Gray Scale Filter first !")
            selected_var.set(GrayTabChoice.Empty.value)
            self.view.editor_menu.gray_filters_tab.was_selected=GrayTabChoice.Empty.value
            return
        is_disable_action=old==selected_var.get()
        is_threshold_last=old==GrayTabChoice.Threshold.value
        is_threshold_current=selected_var.get()==GrayTabChoice.Threshold.value
        
        if (is_disable_action):
            selected_var.set(GrayTabChoice.Empty.value)
        if(is_threshold_last):
            threshold_entry.delete(0,END)
            threshold_entry.configure(state='disabled')
        self.remove_event(match=lambda event:event in self.gray_tab_effects_dict.values())
        if is_threshold_current and not is_disable_action:
                threshold_entry.configure(state='normal')      
        elif  not is_disable_action:
                self.add_or_update_event(event=(self.gray_tab_effects_dict[selected_var.get()],(None)),
                                             match=lambda event:event in self.gray_tab_effects_dict.values())
        self.view.editor_menu.gray_filters_tab.was_selected=selected_var.get()
        self.model.apply_edits(self.events)
        self.update_view_edited_container()
    
    def sharpening_handler(self):
        old= self.view.editor_menu.sharpening_tab.was_selected
        selected_var:IntVar=self.view.editor_menu.sharpening_tab.selected_var
        is_disable_action=old==selected_var.get()
        if (is_disable_action):
            selected_var.set(SharpeningChoice.Empty.value)
        self.remove_event(match=lambda event:event ==self.model.sharpening)
        if(not is_disable_action):
            self.add_or_update_event(event=(self.model.sharpening,(selected_var.get())),
                                             match=lambda event:event ==self.model.sharpening)
        self.view.editor_menu.sharpening_tab.was_selected=selected_var.get()
        self.model.apply_edits(self.events)
        self.update_view_edited_container()
    
    def smoothing_handler(self):
        old= self.view.editor_menu.smoothing_tab.was_selected
        selected_var:IntVar=self.view.editor_menu.smoothing_tab.selected_var
        is_disable_action=old==selected_var.get()
        if (is_disable_action):
            selected_var.set(SmoothingChoice.Empty.value)
        self.remove_event(match=lambda event:event in self.smoothing_tab_effects_dict.values())
        if(not is_disable_action):
            self.add_or_update_event(event=(self.smoothing_tab_effects_dict[selected_var.get()],(None)),
                                            match=lambda event:event in self.smoothing_tab_effects_dict.values())
        self.view.editor_menu.smoothing_tab.was_selected=selected_var.get()
        self.model.apply_edits(self.events)
        self.update_view_edited_container()
    def noise_handler(self):
        sp_amount_entry:CTkEntry=self.view.editor_menu.noise_tab.sp_amount_entry
        old= self.view.editor_menu.noise_tab.was_selected
        selected_var:IntVar=self.view.editor_menu.noise_tab.selected_var
        
        if self.view.editor_menu.gray_filters_tab.gray_switch.get() == 0:
            messagebox.showinfo("info", "Enable Gray Scale Filter first !")
            selected_var.set(NoiseChoice.Empty.value)
            self.view.editor_menu.noise_tab.was_selected=NoiseChoice.Empty.value
            return
        is_disable_action=old==selected_var.get()
        is_sp_last=old==NoiseChoice.SP.value
        is_sp_current=selected_var.get()==NoiseChoice.SP.value
        
        if (is_disable_action):
            selected_var.set(GrayTabChoice.Empty.value)
        if(is_sp_last):
            sp_amount_entry.delete(0,END)
            sp_amount_entry.configure(state='disabled')
        self.remove_event(match=lambda event:event in [self.model.gaussian_noise,self.model.sp_noise])
        if is_sp_current and not is_disable_action:
                sp_amount_entry.configure(state='normal')      
        elif  not is_disable_action:
                self.add_or_update_event(event=(self.model.gaussian_noise,(None)),
                                         match=lambda event:event in [self.model.gaussian_noise,
                                                                      self.model.sp_noise])
    
        self.view.editor_menu.noise_tab.was_selected=selected_var.get()
        self.model.apply_edits(self.events)
        self.update_view_edited_container()
    def sp_handler(self,event):
        entry:CTkEntry=self.view.editor_menu.noise_tab.sp_amount_entry
        content: str = entry.get().replace(" ", "")
        result = self.validate_float_content(content)
        entry.delete(0, END)
        if result == ValidationResult.NotValid or result == ValidationResult.Empty:
            self.remove_event(match=lambda event:event==self.model.sp_noise)
        if result == ValidationResult.NotValid:
            messagebox.showerror("Error", "Enter an float value  from 0 to 1!")
        if result == ValidationResult.Valid:
            param = float(content)
            self.add_or_update_event(event=(self.model.sp_noise, (param)),
                                    match=lambda event:event==self.model.sp_noise)
            entry.insert(0, param)

        self.model.apply_edits(self.events)
        self.update_view_edited_container()

    def edge_handler(self):
        old= self.view.editor_menu.edge_detection_tab.was_selected
        selected_var:IntVar=self.view.editor_menu.edge_detection_tab.selected_var
        is_disable_action=old==selected_var.get()
        if self.view.editor_menu.gray_filters_tab.gray_switch.get() == 0:
            messagebox.showinfo("info", "Enable Gray Scale Filter first !")
            selected_var.set(EdgeDetectionChoice.Empty.value)
            self.view.editor_menu.edge_detection_tab.was_selected=EdgeDetectionChoice.Empty.value
            return
        
        if (is_disable_action):
            selected_var.set(EdgeDetectionChoice.Empty.value)
        self.remove_event(match=lambda event:event in self.edge_tab_effects_dict.values())
        if(not is_disable_action):
            self.add_or_update_event(event=(self.edge_tab_effects_dict[selected_var.get()],(None)),
                                            match=lambda event:event in self.edge_tab_effects_dict.values())
        self.view.editor_menu.edge_detection_tab.was_selected=selected_var.get()
        self.model.apply_edits(self.events)
        self.update_view_edited_container()
    def validate_float_content(self,content:str):

        # if content and content[0]=='-':
        #     return ValidationResult.NotValid
        value:float=None
        try:
            value=float(content)
        except:
            if not content:
                return ValidationResult.Empty
            return ValidationResult.NotValid
        if value==0:
            return ValidationResult.Empty
        if value >0 and value<=1 :
            return ValidationResult.Valid
        return ValidationResult.NotValid
    def validate_content(self, content: str, match_regex: str) -> ValidationResult:
        is_valid = bool(match(match_regex, content))

        if is_valid:
            return ValidationResult.Valid
        if not content or match(r"^0+$", content):
            return ValidationResult.Empty
        return ValidationResult.NotValid
    def validate_uncoupled_entries(
        self,current_entry: CTkEntry,another_entry:CTkEntry, regex: str,reversed:bool, error_message: str, event, event_match
    ):
        content: str = current_entry.get().replace(" ", "")
        result = self.validate_content(content, regex)
        current_entry.delete(0, END)
        if (result == ValidationResult.NotValid or result == ValidationResult.Empty ) and another_entry.get()=='':
            self.remove_event(match=event_match)
        if result == ValidationResult.NotValid:
            another_entry.delete(0, END)
            messagebox.showerror("Error", error_message)
        if result == ValidationResult.Valid or another_entry.get():
            param=int(content) if content else 0
            if result==ValidationResult.Valid:
                current_entry.insert(0,param )
            another_param=int(another_entry.get()) if another_entry.get() else 0
            params =(another_param,param) if reversed else (param,another_param)
            self.add_or_update_event(event=(event, params), match=event_match)

        self.model.apply_edits(self.events)
        self.update_view_edited_container()
    
    def validate_coupled_entries(
        self,current_entry: CTkEntry,another_entry:CTkEntry, regex: str,reversed:bool, error_message: str, event, event_match
    ):
        content: str = current_entry.get().replace(" ", "")

        result = self.validate_content(content, regex)
        current_entry.delete(0, END)
        if result == ValidationResult.NotValid or result == ValidationResult.Empty:
            self.remove_event(match=event_match)
        if result == ValidationResult.NotValid:
            another_entry.delete(0, END)
            messagebox.showerror("error", error_message)
        if result == ValidationResult.Valid:
            param=int(content)
            current_entry.insert(0,param )
            if not another_entry.get():
               return
            params =(int(another_entry.get()),param) if reversed else (param,int(another_entry.get()))
            self.add_or_update_event(event=(event, params), match=event_match)

        self.model.apply_edits(self.events)
        self.update_view_edited_container()
    
    def validate_entry(
        self, entry: CTkEntry, regex: str, error_message: str, event, event_match
    ):
        content: str = entry.get().replace(" ", "")
        result = self.validate_content(content, regex)
        entry.delete(0, END)

        if result == ValidationResult.NotValid or result == ValidationResult.Empty:
            self.remove_event(match=event_match)
        if result == ValidationResult.NotValid:
            messagebox.showerror("Error", error_message)
        if result == ValidationResult.Valid:
            param = int(content)
            self.add_or_update_event(event=(event, (param)), match=event_match)
            entry.insert(0, param)

        self.model.apply_edits(self.events)
        self.update_view_edited_container()
    
  
# def gray_radio_handler2(self):
#         old= self.view.editor_menu.gray_filters_tab.was_selected
#         selected_var:IntVar=self.view.editor_menu.gray_filters_tab.selected_var
#         if self.view.editor_menu.gray_filters_tab.gray_switch.get() == 0:
#             messagebox.showinfo("Note", "Enable Gray Scale Filter first !")
#             selected_var.set(GrayTabChoice.Empty.value)
#             self.view.editor_menu.gray_filters_tab.was_selected=GrayTabChoice.Empty.value
#             return
#         if (old==selected_var.get()):
#             selected_var.set(GrayTabChoice.Empty.value)
#             self.view.editor_menu.gray_filters_tab.was_selected= selected_var.get()
#             if(old==GrayTabChoice.Threshold.value):
#                 self.view.editor_menu.gray_filters_tab.threshold_entry.delete(0,END)
#                 self.view.editor_menu.gray_filters_tab.threshold_entry.configure(state='disabled')
#             self.remove_event(match=lambda event:event in self.gray_tab_effects_dict.values())
#         else:
#             if old==GrayTabChoice.Threshold.value:
#                 self.view.editor_menu.gray_filters_tab.threshold_entry.delete(0,END)
#                 self.view.editor_menu.gray_filters_tab.threshold_entry.configure(state='disabled')
#             self.remove_event(match=lambda event:event in self.gray_tab_effects_dict.values())

#             if selected_var.get()!=GrayTabChoice.Threshold.value:
#                 self.add_or_update_event(event=(self.gray_tab_effects_dict[selected_var.get()],(None)),
#                                              match=lambda event:event in self.gray_tab_effects_dict.values())
#             else:
#                 self.view.editor_menu.gray_filters_tab.threshold_entry.configure(state='normal')
#         self.view.editor_menu.gray_filters_tab.was_selected=selected_var.get()
#         self.model.apply_edits(self.events)
#         self.update_view_edited_container()
            
            
# endregion
# def gray_radio_handler3(self):
#         threshold_entry:CTkEntry=self.view.editor_menu.gray_filters_tab.threshold_entry
#         old= self.view.editor_menu.gray_filters_tab.was_selected
#         selected_var:IntVar=self.view.editor_menu.gray_filters_tab.selected_var
        
#         if self.view.editor_menu.gray_filters_tab.gray_switch.get() == 0:
#             messagebox.showinfo("info", "Enable Gray Scale Filter first !")
#             selected_var.set(GrayTabChoice.Empty.value)
#             self.view.editor_menu.gray_filters_tab.was_selected=GrayTabChoice.Empty.value
#             return
        
#         is_disable_action=old==selected_var.get()
#         is_threshold_last=old==GrayTabChoice.Threshold.value        
#         if (is_disable_action):
#             selected_var.set(GrayTabChoice.Empty.value)
#         if(is_threshold_last):
#             threshold_entry.delete(0,END)
#             threshold_entry.configure(state='disabled')
#         self.remove_event(match=lambda event:event in self.gray_tab_effects_dict.values())
#         if selected_var.get()==GrayTabChoice.Threshold.value and not is_disable_action:
#                 threshold_entry.configure(state='normal')      
#         elif  not is_disable_action:
#                 self.add_or_update_event(event=(self.gray_tab_effects_dict[selected_var.get()],(None)),
#                                              match=lambda event:event in self.gray_tab_effects_dict.values())
#         self.view.editor_menu.gray_filters_tab.was_selected=selected_var.get()
#         self.model.apply_edits(self.events)
#         self.update_view_edited_container()
