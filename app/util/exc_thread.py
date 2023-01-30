import threading
import ctypes


class ExcThread(threading.Thread):
    """
    Advantages of using `ExcThread`.
    * Stop the running thread whenever you want.
    * You can stop the all running threads of `ExcThread`.

    """

    def __init__(self, group=None, target=None, name=None,
        args=(), kwargs=None, *, daemon=None, standalone: bool=False) -> None:
        super().__init__(group=group, target=target, name=name,
            args=args, kwargs=kwargs, daemon=daemon)
        
        self.standalone = standalone
    
    def __getid(self) -> int:
        if hasattr(self, "_thread_id"):
            return self._thread_id
        
        for id, thread in threading._active.items():
            if thread is self:
                return id
    
    def stop(self) -> None:
        """
        Stop the running thread `self`
        """
        t_id = self.__getid()
        res = ctypes.pythonapi.PyThreadState_SetAsyncExc(t_id, ctypes.py_object(SystemExit))

        if res > 1:
            ctypes.pythonapi.PyThreadState_SetAsyncExc(t_id, 0)
            print(f"{self.name}: Exception raise failure")

    @staticmethod
    def exit(exit_main: bool = False, status_code: int = ...) -> None:
        """
        This `@staticmethod` function will stop all running `ExcThread` except `standalone` thread
        and also MainThread if you say.
        * exit_main: If `True` then this will raise the SystemExit with the status code (`SystemExit(status_code)`)
        default code zero.
        * return: None
        """
        threads: list[ExcThread] = list(filter(lambda t: isinstance(t, ExcThread), [t for _, t in threading._active.items()]))
        
        for thread in threads:
            if not thread.standalone:
                thread.stop()
        
        if exit_main:
            raise SystemExit(status_code if status_code != ... else 0)
            


if __name__ == "__main__":
    pass