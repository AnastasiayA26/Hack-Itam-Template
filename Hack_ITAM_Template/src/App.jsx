import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import './App.css';
import NotFound from './Pages/NotFoundPage';
import Layout from './components/Layout';
import UserPage from './Pages/UserPage';
import HackatonsPage from './Pages/HackatonsPage';
import UsefullMaterialsPage from './Pages/UsefullMaterials';
import HackatonPage from './Pages/HackatonPage';

function App() {
  return (
    <Router>
      <Layout>
        <Routes>
          <Route
            path="/"
            element={
              <>
                <h1>here was Wokka</h1>
              </>
            }
          />
          <Route path="/test" element={<h1> There`s something testing</h1>} />
          <Route path="/hackatons/" element={<HackatonsPage />} />
          <Route path="/hackatons/:id" element={<HackatonPage />} />
          <Route path="*" element={<NotFound />} />
          <Route path="/Materials" element={<UsefullMaterialsPage />} />
          <Route path="/user/:id" element={<UserPage />} />
        </Routes>
      </Layout>
    </Router>
  );
}

export default App;
