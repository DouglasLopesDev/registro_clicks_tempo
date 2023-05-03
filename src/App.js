import logo from './logo.svg';
import './App.css';
// import { getCurrentDate } from './utils'
import { useState, useEffect } from "react";
import Button from "./components/button/Button"
import Input from "./components/input/Input"
import History from "./components/history/History"



function App() {
  const [cliques, setCliques] = useState(0)
  const [searchValue, setSearchValue] = useState()
  const [horarios, setHorarios] = useState([])

  useEffect(() => {
    if (cliques != 0){
      let date = new Date().toJSON();
      setHorarios([...horarios, date])
    }
  }, [cliques])

  const getGlossaryHistory = () => {
    return horarios.map((item) => {
      return (
        <div>
          <p style={{ fontSize: "medium" }}>
            Posição: {horarios.indexOf(item)}  -  Horário: {item} <br />
          </p>
        </div>
      );
    });
  };

  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <hr style={{width:"1000px"}}/>
          <div style={{display:"flex"}}>
            <div style={{marginRigth: "10000px"}}>
              <div>
                <Button
                  name="Clique Aqui"
                  type="primary"
                  style={{ width: "100%", backgroundColor: "green" }}
                  execute={() => {
                    setCliques(parseInt(cliques) + 1);
                  }}
                />
              </div>
              <div>
                <Input
                  fieldName="Pesquisa"
                  type="text"
                  onChange={setSearchValue}
                  name="search"
                  value={searchValue}
                />
                 <Button
                  name="Reiniciar"
                  type="primary"
                  style={{ width: "100%", backgroundColor: "green" }}
                  execute={() => {
                    setCliques(0);
                    setSearchValue("");
                    setHorarios([])
                  }}
                />
                <label>{horarios[searchValue]}</label>
              </div>

            </div>
          <div style={{marginLeft: "109px"}}>
            <History>{getGlossaryHistory()}</History>
          </div>
          </div>

      </header>
    </div>
  );
}

export default App;
