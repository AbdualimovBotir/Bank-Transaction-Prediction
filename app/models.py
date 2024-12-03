import pickle
from sklearn.linear_model import LinearRegression

class TransactionModel:
    def __init__(self, model_path='transaction_model.pkl'):
        """
        Modelni yuklash uchun klass.
        :param model_path: Modelning fayl yo'li
        """
        self.model_path = model_path
        self.model = None
        self.load_model()

    def load_model(self):
        """
        Modelni fayldan yuklash
        """
        try:
            with open(self.model_path, 'rb') as file:
                self.model = pickle.load(file)
            print("Model muvaffaqiyatli yuklandi.")
        except Exception as e:
            print(f"Modelni yuklashda xatolik yuz berdi: {e}")

    def predict(self, transaction_count):
        """
        Tranzaksiya soniga asoslangan holda qiymatni bashorat qilish.
        :param transaction_count: Tranzaksiya soni
        :return: Modelning bashorati
        """
        if self.model is None:
            raise ValueError("Model yuklanmagan.")
        
        # Modelni ishlatib, bashorat qilish
        prediction = self.model.predict([[transaction_count]])
        return prediction[0]
