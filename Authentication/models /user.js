const mongoose = require("mongoose")

const userSchema = new mongoose.Schema({
    name: {
        type: String,
        required: true,
        maxlength: 32,
        trim: true
    },
    lastname: {
        type: String,
        maxlength: 32, 
        trim: true
    },
    email: {
        type: String,
        trim: trim,
        required: true,
        unique: true
    }
})