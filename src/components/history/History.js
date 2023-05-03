import "./History.css";

const History = (props) => {

  return (
    <>
      <div className="Container-history">
        {props.children}
      </div>
    </>
  );
};

export default History;
