import "./forminput.css"

const Forminput = (props) => {
    return (
        <div className="forminput">
            {/* <label>Username</label> */}
            <input placeholder={props.placeholder} onChange={e=>props.setUsername(e.target.value)} />
        </div>
    )
}

export default Forminput