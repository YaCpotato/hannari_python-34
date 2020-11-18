def set_child_watcher(self, watcher):
        """Set the watcher for child processes."""

        assert watcher is None or isinstance(watcher, AbstractChildWatcher)

        if self._watcher is not None:
            self._watcher.close()

        self._watcher = watcher 