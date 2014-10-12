import sublime, sublime_plugin

class ReloadAllFilesCommand(sublime_plugin.WindowCommand):
    def run(self):
        # Run command after 1sec (i.e. wait for SASS to compile CSS)
        sublime.set_timeout(self.focus_all_views, 1000);

    def focus_all_views(self):
        window = self.window
        # Remember current view
        current_view = window.active_view()
        # Save group number
        gr_number = window.num_groups()

        # Loop through all groups
        for i in range(0, gr_number):
            # Focus group
            window.focus_group(i)
            # Save views in that group
            views_in_i = window.views_in_group(i)
            # Focus all views here
            for inner_view in views_in_i:
               window.focus_view(inner_view)

        # Back to current view
        window.focus_view(current_view)
