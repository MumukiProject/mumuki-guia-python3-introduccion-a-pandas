class Test(unittest.TestCase):

  def test_primera_libreria_es_un_series(self):
    self.assertEquals(type(primera_libreria), pd.Series)
    
  def test_segunda_y_tercera_libreria_es_un_dataFrame(self):
    self.assertEquals(type(segunda_y_tercera_libreria), pd.DataFrame)
        
  def test_ultima_libreria_es_un_series(self):
    self.assertEquals(type(ultima_libreria), pd.Series)
    
  def test_primera_libreria_tiene_los_contenidos_correctos(self):
    self.assertEquals(primera_libreria.to_dict(), librerias.iloc[0].to_dict(), "no es el valor correcto")
    
  def test_segunda_y_tercera_libreria_tiene_los_contenidos_correctos(self):
    self.assertEquals(segunda_y_tercera_libreria.to_dict(), librerias.iloc[1:3].to_dict())
        
  def test_ultima_libreria_tiene_los_contenidos_correctos(self):
    self.assertEquals(ultima_libreria.to_dict(), librerias.iloc[-1].to_dict())
    
