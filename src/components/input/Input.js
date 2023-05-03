import "./Input.css";

const Input = (props) => {
  return (
    <>
      <label style={{ ...props.style }} className="Label">
        {props.fieldName}:
        <input
          className="Input"
          onChange={(event) => props.onChange(event.target.value)}
          type={props.type}
          name={props.nameValue}
          value={props.value}
        />
      </label>
      <br />
    </>
  );
};

export default Input;
