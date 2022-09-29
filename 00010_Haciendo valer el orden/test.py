import pandas as pd

class Test(unittest.TestCase):

  def test_cines_mas_amplios_es_un_dataFrame(self):
    self.assertEquals(type(cines_mas_amplios), pd.DataFrame)
    
  def test_cines_mas_amplios_tiene_tres_filas(self):
    self.assertEquals(len(cines_mas_amplios), 3)    