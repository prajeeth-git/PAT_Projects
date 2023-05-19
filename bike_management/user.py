class user:

    def __init__(self):
        self.models={
            'R15M ':{'Price':'Rs.1.81 - 1.94 Lakh*','Engine':'249cc','Power':'20.8PS','Mileage':'50.33kmpl','Brakes':'Double Disc','Tyre Type':'Tubeless'},
            'R15 V4 ':{'Price':'Rs.1.81 - 1.94 Lakh*','Engine':'155cc','Power':'18.4PS','Mileage':'55.20kmpl','Brakes':'Double Disc','Tyre Type':'Tubeless'},
            'R15S ':{'Price':'Rs.1.63 Lakh*','Engine':'155cc','Power':'18.6PS','Mileage':'40kmpl','Brakes':'Double Disc','Tyre Type':'Tubeless'},
            'MT-15 Ver 2.0':{'Price':'Rs.1.65 - 1.69 Lakh*','Engine':'155cc','Power':'18.4PS','Mileage':'56.87kmpl','Brakes':'Double Disc','Tyre Type':'Tubeless'},
            'FZ 25':{'Price':'Rs.1.50 Lakh*','Engine':'249cc','Power':'20.8PS','Mileage':'50.33kmpl','Brakes':'Double Disc','Tyre Type':'Tubeless'}
        }

    def displaymodels(self):
        return self.models.keys()
    
    def bikedetails(self,model):
        print("model:",model)
        print('Price:',self.models[model]["Price"],'\n','Engine:',self.models[model]["Engine"],'\n','Power:',self.models[model]["Power"],'\n','Mileage:',self.models[model]["Mileage"],'\n','Brakes:',self.models[model]["Brakes"],'\n','Tyre Type:',self.models[model]["Tyre Type"],'\n')



    
