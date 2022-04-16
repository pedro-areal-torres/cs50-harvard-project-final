var express = require('express');
var Tarefa = require('../models/Tarefa');
var router = express.Router();
var request = require("request");

// on routes that end in /tarefas
// ----------------------------------------------------
router.route('/')
    .get((req, res) => {
        Tarefa.find((err, tarefas) => {
            if (err) {
                res.send(err);
            }

            res.json({
                tarefas
            });
        });
    })
    .post((req, res) => {
        if (typeof req.body.nome === 'undefined') {
            res.sendStatus(400);
        } else {
            var t = new Tarefa();
            t.orderNum = req.body.orderNum;
            t.nome = req.body.nome;
            t.descricao = req.body.descricao;
            t.interveniente = req.body.interveniente;
            t.id = makeid(5);
            t.save((err, tar) => {
                if (err) {
                    res.send(err);
                }

                res.json({
                    message: "Object Created!",
                    object: tar
                });
            });

        }
    })

    .delete((req, res) => {
        if (typeof req.body.id === 'undefined') {
            res.sendStatus(400);
        } else {
            Tarefa.deleteOne({id: req.body.id},(err, tar) => {
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

router.route('/all')
    .delete((req, res) => {
        Tarefa.deleteMany({},(err, tar) => {
            if (err) {
                res.send(err);
            }

            res.json({
                message: "Object Deleted!",
                object: tar
            });
        });
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