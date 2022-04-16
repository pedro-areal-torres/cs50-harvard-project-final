var express = require('express');
var OrdemTrabalho = require('../models/OrdemTrabalho');
var Tarefa = require('../models/Tarefa');
var router = express.Router();
var request = require("request");

// on routes that end in /ordemTrabalho
// ----------------------------------------------------
router.route('/chefeManutencao')
    .get((req, res) => {
        OrdemTrabalho.find((err, ords) => {
            if (err) {
                res.send(err);
            }

            var orders = ords.map(function (x) {
                return {
                    id: x.id,
                    orderNum: x.orderNum,
                    titulo: x.titulo,
                    tipo: x.tipo,
                    custoEstimado: x.custoEstimado
                }
            });


            res.json({
                orders
            });
        });
    })

    .post((req, res) => {
        if (typeof req.body.titulo === 'undefined' ) {
            res.sendStatus(400);
        } else {
            var o = new OrdemTrabalho();
            o.orderNum = req.body.orderNum;
            o.titulo = req.body.titulo;
            o.descricao = req.body.descricao;
            o.dataCriacao = new Date();
            o.tipo = req.body.tipo;
            o.custoEstimado = req.body.custoEstimado;
            o.dataComeco = req.body.dataComeco;
            o.dataPrevistaFim = req.body.dataPrevistaFim;
            o.prioridadeOrdem = req.body.prioridadeOrdem;
            o.id = makeid(5);

            o.save((err, eq) => {
                if (err) {
                    res.send(err);
                }

                res.json({
                    message: "Object Created!",
                    object: eq
                });
            });
        };
    })
    
    .delete((req, res) => {
        console.log("MYRIAM")
        console.log(req.body.id)
        if (typeof req.body.id === 'undefined') {
            res.sendStatus(400);
        } else {
            
            
            OrdemTrabalho.deleteOne({id: req.body.id},(err, tar) => {
                if (err) {
                    res.send(err);
                }

                res.json({
                    message: "Object Deleted!",
                    object: tar
                });
            });
        }
    });


module.exports = router;

function makeid(length) {
    var result = '';
    var characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789';
    var charactersLength = characters.length;
    for (var i = 0; i < length; i++) {
        result += characters.charAt(Math.floor(Math.random() * charactersLength));
    }
    return result;
}