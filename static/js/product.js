const mongoose = require ("mongoose")
const schema =  mongoose.Schema

const productSchema = new Schema ({
    id:{
        type: Number ,
        required: true
    },
    title :{
        type : String,
        required: true
    },
    price : {
        type :Number ,
        required : true
    },
    descript : String,
    category : String,
    image : String
})
module.exports = mongoose.model('product',productSchema)
