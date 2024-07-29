import time
from flow_panel.flow_panel import FlowPanel

if __name__ == "__main__":

    def example_run_function(panel: FlowPanel):
        panel.update_progress(0, 10)
        for i in range(10):
            if panel.should_stop or panel.stop_event.is_set():
                break
            time.sleep(1)
            panel.update_progress(i + 1, 10)
            panel.append_message(f"Step pass {i + 1} completed.")
        panel.append_message("Process finished.")

    gui = FlowPanel(
        title_short="Test Panel",
        title_long="Test Panel GUI",
        list_descriptions=["Run a test process", "with multiple steps."],
        list_user_entries=[
            ["Input 1", "entry", True, None],
            ["Input 2", "combobox", False, ["Option 1", "Option 2"]],
            ["Input 3", "checkbox", False, None],
        ],
        run_function=example_run_function,
        help="This is an example help text."
    )
    gui.mainloop()
