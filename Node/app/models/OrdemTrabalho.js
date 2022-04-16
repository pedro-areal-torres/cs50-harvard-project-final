// get an instance of mongoose and mongoose.Schema
var mongoose = require('mongoose');
var Schema = mongoose.Schema;

// set up a mongoose model and pass it using module.exports
var OrdemTrabalhoSchema = new Schema({
    orderNum: String,
    titulo: String,
    descricao: String,
    tipo: String,
    custoEstimado: Number,
    dataCriacao: String,
    dataComeco: String,
    dataPrevistaFim: String,
    prioridadeOrdem: String,
    id: String

}, { usePushEach: true });

OrdemTrabalhoSchema.set('toJSON', {
    virtuals: true,
    transform: (doc, ret, options) => {
        delete ret.__v;
        delete ret._id;
    },
});

module.exports = mongoose.model('OrdemTrabalho',OrdemTrabalhoSchema);