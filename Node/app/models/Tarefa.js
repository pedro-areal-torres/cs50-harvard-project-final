// get an instance of mongoose and mongoose.Schema
var mongoose = require('mongoose');
var Schema = mongoose.Schema;

// set up a mongoose model and pass it using module.exports
var TarefaSchema = new Schema({
    orderNum: String,
    nome: String,
    descricao: String,
    interveniente: String,
    id: String
}, { usePushEach: true });

TarefaSchema.set('toJSON', {
    virtuals: true,
    transform: (doc, ret, options) => {
        delete ret.__v;
        delete ret._id;
    },
});

module.exports = mongoose.model('Tarefa', TarefaSchema);