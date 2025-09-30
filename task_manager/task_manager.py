
class TaskManager:

    tasks:dict[str,dict]
    task_id:str #chiave del dizionario

    def __init__(self)-> None:
        
        self.tasks:dict[str,dict[str,dict|bool]] = {}

        
    def create_task(self, task_id:str, descrizione:str) -> str|dict[str,dict[str,bool]]:

        if task_id in self.task_id:

            raise ValueError("Errore il task esiste gia")
        else:

            temp_dict = {
                "descrizione":descrizione,
                "completato":False
                }
        
            self.tasks[task_id] = temp_dict

        return {task_id:temp_dict}
    
    def complete_task(self, task_id:str) -> dict|str:

        if task_id not in self.tasks:
            return "TAsk non presente"
        else:
            self.tasks[task_id]["completato"] = True
        
            return {task_id:self.tasks[task_id]}
    
    def update_description(self,task_id:str, nuova_descrizione:str) -> dict|str:

        if task_id not in self.tasks:
            return "Task non presente"

        else:

            self.tasks[task_id]["descrizione"] = nuova_descrizione

        return {task_id:self.tasks[task_id]}

    def remove_task(self, task_id:str)-> dict|str:

        if task_id not in self.tasks:
            return "TASKNONPRESENTE"
        else:
            key, value = self.tasks.popitem(task_id)

            return {key:value}
        
    def list_task(self) -> list[str]:

        return list(self.tasks)
    
    def get_task(self,task_id:str)-> dict|str:

        if task_id not in self.task:
            return "EROOORO"
        else:
            return self.tasks[task_id]


