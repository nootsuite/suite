# NootSuite
quick and dirty privacy suite powered by python + flask, deployable in a single touch
## How the fudge does it work?
Look at this nice flowchart of the `PinguHTTP` model
```mermaid
flowchart
    a[User sends request] -->|Hey, can I have example.com| b(Server recieves request)
    b --> c{Is request valid?}
    d{Is request a valid file?}
    c -->|No| ire[Return InvalidReqError]
    c --> |Yes| f(Return page)
    d -->|No| ire
    f --> g(Standby for more requests)
    g -->|Hey, I need this file!| e{Is file a valid file?} -->|Yes|h(Return the file) --> g
    e -->|No| ire
```
## How do I contribute?
`open a pull request, for god's sake`
If you make enough contributions, you might become a posh collaborator!
