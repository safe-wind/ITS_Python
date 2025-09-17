from dottore import Dottore


class Fattura:

    def __init__(self, patients:list[str], doctor:Dottore):

        if doctor.isAValidDoctor():
            self._doctor = doctor
            self._patients = patients
            self._fatture = len(patients)
            self.salary = 0
        else:
            self._doctor = None
            self._patients = None
            self._fatture = None
            self.salary = None

    def getSalary(self):
        if self._doctor and self._patients is not None:
            self.salary = int((self._doctor.getParcel()) * (len(self._patients)))

    def getFatture(self):
        if self.patients is not None:
            self.fatture = len(self.patients)
            return self.fatture
        return None

    def addPatient(self, newPatient):
        if self.patients is not None:
            self.patients.append(newPatient)
            self.getFatture()
            self.getSalary()
            print(f"Alla lista del Dottor {self.doctor.cognome} è stato aggiunto il paziente {newPatient.getidCode()}")

    def removePatient(self, idCode):
        if self.patients is not None:
            for p in self.patients:
                if p.getidCode() == idCode:
                    self.patients.remove(p)
                    self.getFatture()
                    self.getSalary()
                    print(f"Alla lista del Dottor {self.doctor.cognome} è stato rimosso il paziente {idCode}")
                    break