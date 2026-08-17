import sys

from view.main_view import PolisherView

from model.light_model import LightModel
from model.lissa_model import LissaModel
from presenter.light_presenter import LightPresenter
from presenter.lissa_presenter import LissaPresenter
from model.pad_model import PadModel
from presenter.pad_presenter import PadPresenter
from model.column_model import ColumnModel
from presenter.column_presenter import ColumnPresenter

# --- Hardware configuration ---
PIN_LIGHT_GPIO = 18
PIN_LISSA_GPIO = 26

PIN_PAD_PWM = 12
PIN_PAD_CW = 13
PIN_PAD_CCW = 6

PIN_COL_PWM = 19
PIN_COL_DIR = 5


def main():
    print("Starting Fiber Polisher System V2...")

    app = None
    light_model = None
    lissa_model = None
    pad_model = None
    col_model = None

    try:
        # 1. Create the GUI.
        app = PolisherView()

        # 2. Initialize hardware. Keeping references initialized to None lets
        # the cleanup block safely close anything that was created before a
        # later hardware initialization failed.
        light_model = LightModel(pin_number=PIN_LIGHT_GPIO)
        lissa_model = LissaModel(pin_number=PIN_LISSA_GPIO)
        pad_model = PadModel(
            pwm_pin=PIN_PAD_PWM,
            cw_pin=PIN_PAD_CW,
            ccw_pin=PIN_PAD_CCW,
        )
        col_model = ColumnModel(en_pin=PIN_COL_PWM, dir_pin=PIN_COL_DIR)

        # 3. Connect presenters to the view and models.
        p_light = LightPresenter(model=light_model, view=app)
        p_lissa = LissaPresenter(model=lissa_model, view=app)
        p_pad = PadPresenter(model=pad_model, view=app)
        p_col = ColumnPresenter(model=col_model, view=app)

        app.set_presenter(
            light_presenter=p_light,
            lissa_presenter=p_lissa,
            pad_presenter=p_pad,
            column_presenter=p_col,
        )
        print("Presenter linked successfully.")

        # 4. Run the GUI.
        print("Showing GUI...")
        app.mainloop()

    except KeyboardInterrupt:
        print("\nForce stopping by user...")
    except KeyError as exc:
        print(f"UI Binding Error: Widget {exc} not found in View.")
        return 1
    except Exception as exc:
        print(f"Application error: {exc}")
        return 1
    finally:
        # 5. Always release every hardware resource that was successfully
        # initialized, including partially initialized startup failures.
        print("Cleaning up resources...")
        for resource in (col_model, pad_model, light_model, lissa_model):
            if resource is not None:
                try:
                    resource.close()
                except Exception as exc:
                    print(f"Cleanup warning: {exc}")
        print("System shutdown complete. Goodbye!")

    return 0


if __name__ == "__main__":
    sys.exit(main())
