class PadPresenter:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.bind_events()

    def bind_events(self):
        """Find the pad controls and connect their events."""
        self.btn_start = self.view.control_widgets.get("speed_start")
        self.btn_stop = self.view.control_widgets.get("speed_stop")
        self.btn_ccw = self.view.control_widgets.get("speed_dir")
        self.lbl_speed = self.view.control_widgets.get("speed")

        if self.btn_start:
            self.btn_start.configure(command=self.on_start)

        if self.btn_stop:
            self.btn_stop.configure(command=self.on_stop)

        if self.btn_ccw:
            self.btn_ccw.configure(command=self.on_dir_toggle)

    def on_start(self):
        """Start the pad using the currently selected direction."""
        try:
            if not self.lbl_speed:
                return

            speed_val = int(self.lbl_speed.cget("text"))
            speed_val = max(0, min(100, speed_val))

            # Starting must not toggle the direction. The direction button is
            # the source of truth for the user's selected direction.
            is_ccw = bool(self.btn_ccw and "selected" in self.btn_ccw.state())
            self.model.set_direction(is_ccw)
            self.model.set_speed(speed_val)

            if speed_val == 0:
                self.view.lbl_status_speed.configure(
                    text="Speed: 0%", bootstyle="inverse-danger"
                )
            else:
                self.view.lbl_status_speed.configure(
                    text=f"Speed: {speed_val}%", bootstyle="inverse-success"
                )

        except ValueError:
            print("[ERROR] Invalid speed value")

    def on_stop(self):
        """Stop the pad completely."""
        self.model.set_speed(0)
        self.model.stop_rotation()
        self.view.lbl_status_speed.configure(
            text="Speed: 0%", bootstyle="inverse-danger"
        )

    def on_dir_toggle(self):
        """Apply the direction selected by the direction toggle."""
        if self.btn_ccw:
            is_ccw = "selected" in self.btn_ccw.state()

            if is_ccw:
                self.btn_ccw.configure(
                    text="CCW <", bootstyle="outline-warning-toolbutton"
                )
            else:
                self.btn_ccw.configure(
                    text="CW >", bootstyle="outline-secondary-toolbutton"
                )

            self.model.set_direction(is_ccw)
