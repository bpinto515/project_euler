// Initialization and var creation of Express

const express =  require('express')
const app = express()
app.use(express.json())


// HTTP METHODS GET , POST, PUT, DELETE

// TYPES OF PARAMETERS
// Query Parameter: request.query (Filters, Sort, Numbering Pages, ... )
// Route Parameter: request.params (Identify a resource on the change or delete of it)  ) 
// Body : request.body (Data to create or change a registry )

// MONGODB (Non-relational DB)


app.post('/users', (request, response) => {
    console.log(request.body);
    return response.json({message: 'Hello PA'})
})

app.listen(3333)

