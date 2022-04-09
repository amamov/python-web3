function connectAccount() {
    if (window.ethereum) window.ethereum.request({ method: "eth_requestAccounts" })
        .then((accounts) => {
            fetch("/web3", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify({
                    account: accounts[0]
                })
            }).then(res => res.json()).then(res => console.log(res))
                .catch(error => console.error(error))
        })
        .catch(error => console.error(error))
    else alert("Install Metamask!")
}

connectAccount()