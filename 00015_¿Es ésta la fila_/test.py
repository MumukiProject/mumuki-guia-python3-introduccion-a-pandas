class Test(unittest.TestCase):

  def test_primera_libreria_es_un_series(self):
    self.assertEquals(type(primera_libreria), pd.Series)
    
  def test_segunda_y_tercera_libreria_es_un_dataFrame(self):
    self.assertEquals(type(segunda_y_tercera_libreria), pd.DataFrame)
        
  def test_ultima_libreria_es_un_series(self):
    self.assertEquals(type(ultima_libreria), pd.Series)
    
