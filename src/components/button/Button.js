import "./Button.css";

const Button = (props) => {
  return (
    <>
      <button
        style={{ ...props.style }}
        className="Button"
        type={props.type}
        onClick={() => props.execute(...[props.param])}
      >
        {props.name}
      </button>
    </>
  );
};

export default Button;
