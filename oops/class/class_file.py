class Car:
    
    def __init__(self, model, name, year, color):
        self.model = model
        self.name = name
        self.year = year
        self.color = color
        
    def welcome(self):
        print(f'welcome to {self.model}')
        
    def about(self):
        print(f'{self.name} is good car')
        
    def __str__(self):
        return f"Car(model='{self.model}', name='{self.name}', year={self.year}, color='{self.color}')"