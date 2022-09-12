import React, { useState, useEffect } from "react";


const HomePage = () => {
    const [url, setUrl] = useState("Enter your URL here")
    const [response, setResponse] = useState()
    const handleClick = (e) => {
        if (url==="Enter your URL here") setUrl("")
    }
    const handleSubmit = (e) => {
        console.log(url)
        e.preventDefault()
        fetch('/api/', {
            method: 'POST',
            body: JSON.stringify({url}),
            headers: {
                'Content-type': 'application/json; charset=UTF-8'
            }
        })
        .then(res => res.json())
        .then(res => {
            setResponse(res.code ? `${window.location.href}api/${res.code}` : res)
        })
        .catch(err => {
            console.log(err)
        })
    }

    return (
        <div>
            <h1>Shorten your URL</h1>
            <form onSubmit={e => { handleSubmit(e) }}>
                <input type="text" id="url" name="url" value={url} onChange={e => setUrl(e.target.value)} onClick={handleClick}/>
                <div id="submit-div">
                <input type="submit" id="submit-button" value="Shorten!"/>
                </div>
            </form>
            <div id="response-div">{response}</div>
        </div>
        )
}

export default HomePage;