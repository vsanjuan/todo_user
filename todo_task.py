# -*- coding: utf-8 -*-
from openerp import models, fields, api
class TodoTask(models.Model):
	_inherit = 'todo.task'
	user_id = fields.Many2one('res.users', 'Responsible')
	date_deadline = fields.Date('Deadline')
	