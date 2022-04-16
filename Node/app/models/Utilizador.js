// get an instance of mongoose and mongoose.Schema
var mongoose = require('mongoose');
var Schema = mongoose.Schema;

// set up a mongoose model and pass it using module.exports
var UtilizadorSchema = new Schema({
    nome: String,
    password: String,
    postoTrabalho: String,
    permissoes: Number,
    id: String
}, { usePushEach: true });

UtilizadorSchema.set('toJSON', {
    virtuals: true,
    transform: (doc, ret, options) => {
        delete ret.__v;
        delete ret._id;
    },
});

module.exports = mongoose.model('Utilizador', UtilizadorSchema);