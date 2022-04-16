var express = require('express');
var Utilizador = require('../models/Utilizador');
var router = express.Router();
var request = require("request");

// on routes that end in /utilizador
// ----------------------------------------------------
router.route('/register')
    .post((req, res) => {
        if (typeof req.body.nome === 'undefined' || typeof req.body.password === 'undefined') {
            res.sendStatus(400);
        } else {
            var u = new Utilizador();
            u.nome = req.body.nome;
            u.password = req.body.password;
            u.postoTrabalho = 'Manutenção';
            u.permissoes = req.body.permissoes;
            u.id = makeid(5);
            u.save((err, util) => {
                if (err) {
                    res.send(err);
                }

                res.json({
                    message: "User Created!",
                    object: util
                });
            });

        }
    });

router.route('/login')
    .post((req, res) => {
        if (typeof req.body === 'undefined' || typeof req.body.username === 'undefined' || typeof req.body.password === 'undefined') {
            res.sendStatus(400);
        } else {
            Utilizador.findOne({
                nome: req.body.username
            }, (err, util) => {
                if (err) {
                    res.send(err);
                }
                
                var ret;
                if (typeof util === 'undefined' || typeof req.body === 'undefined' || util.password !== req.body.password) {
                    ret = 0;
                } else {
                    ret = util.permissoes;
                }

                res.json({
                    permissoes: ret
                });
            });
        }
    });

    router.route('/users')
    .get((req, res) => {
        Utilizador.find({}, (err, utils) => {
            if (err) {
                res.send(err);
            }
            res.json(utils);
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