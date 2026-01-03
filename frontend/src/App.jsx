import { useState } from 'react'
import axios from 'axios'

function App() {
  const [formData, setFormData] = useState({ area: '', quartos: '', banheiros: '' })
  const [resultado, setResultado] = useState(null)
  const [carregando, setCarregando] = useState(false)

  const handleSubmit = async (e) => {
    e.preventDefault()
    setCarregando(true)
    try {
      const response = await axios.post('http://127.0.0.1:8000/predict', formData)
      setResultado(response.data.preco_estimado)
    } catch (error) {
      alert("Erro ao conectar com o servidor! Verifique se o backend está rodando.")
    } finally {
      setCarregando(false)
    }
  }

  return (
    <div className="min-h-screen bg-[#edecb3] flex items-center justify-center p-4">
      <div className="bg-white rounded-2xl shadow-2xl p-8 w-full max-w-md">
        <h1 className="text-3xl font-extrabold text-slate-800 mb-2 text-center">HouseLytics</h1>
        <p className="text-slate-500 text-center mb-8">Previsão Inteligente de Imóveis</p>

        <form onSubmit={handleSubmit} className="space-y-4">
          <div>
            <label className="block text-sm font-medium text-slate-700 mb-1">Área Total (m²)</label>
            <input 
              type="number" 
              required
              className="w-full border border-slate-300 p-3 rounded-lg focus:ring-2 focus:ring-indigo-500 outline-none transition"
              onChange={e => setFormData({...formData, area: e.target.value})} 
            />
          </div>

          <div className="grid grid-cols-2 gap-4">
            <div>
              <label className="block text-sm font-medium text-slate-700 mb-1">Quartos</label>
              <input 
                type="number" 
                required
                className="w-full border border-slate-300 p-3 rounded-lg focus:ring-2 focus:ring-indigo-500 outline-none transition"
                onChange={e => setFormData({...formData, quartos: e.target.value})} 
              />
            </div>
            <div>
              <label className="block text-sm font-medium text-slate-700 mb-1">Banheiros</label>
              <input 
                type="number" 
                required
                className="w-full border border-slate-300 p-3 rounded-lg focus:ring-2 focus:ring-indigo-500 outline-none transition"
                onChange={e => setFormData({...formData, banheiros: e.target.value})} 
              />
            </div>
          </div>

          <button 
            type="submit"
            disabled={carregando}
            className="w-full bg-[#00686c] text-white font-bold py-4 rounded-lg hover:bg-[#32c2b9] transition-all shadow-lg active:scale-95 disabled:bg-slate-400"
          >
            {carregando ? 'Calculando...' : 'Obter Estimativa'}
          </button>
        </form>

        {resultado && (
          <div className="mt-8 p-4 bg-emerald-50 border border-[#ff9915] rounded-xl text-center">
            <span className="text-[#ff9915] font-semibold block uppercase text-xs tracking-wider">Preço Sugerido</span>
            <span className="text-3xl font-black text-[#ff9915]">
              R$ {resultado.toLocaleString('pt-BR')}
            </span>
          </div>
        )}
      </div>
    </div>
  )
}

export default App