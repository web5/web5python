# -*- coding: utf-8 -*-

from datetime import datetime
from webcore.utils.db import db
from webcore.utils import get_current_user
from webcore.utils import slugify

class Dated(object):
    available_time = db.Column(db.DateTime, default=datetime.now)
    availabel_until = db.Column(db.DateTime,
                                default=datetime.now, required=False)
    create_time = db.Column(db.DateTime, default=datetime.now)
    update_time = db.Column(db.DateTime, default=datetime.now)

class Own(object):
    user = db.relationship('User')
    created_by = db.Column(db.Integer, db.ForeignKey('user.id'), required=True)
    updated_by = db.Column(db.Ingeger, db.ForeignKey('user.id'), required=True)

class Published(Dated, Own):
    published = db.Column(db.Integer, default=False)

    def save(self, *args, **kwargs):
        self.update_time = datetime.now
        user = get_current_user()

        if not user.id:
            self.created_by = user.id
        self.update_by = user.id
        super(Published, self).save(*args, **kwargs)

class Slug(object):
    slug = db.Column(db.String(255), required=True)
    def validate_slug(self, title=None):
        if self.slug:
            self.slug = slugify(self.slug)
        else:
            self.slug = slugify(title or self.title)

class LongSlug(Slug):

    log_slug = db.Column(db.String(255), required=True)
    mpath = db.Column(db.String)

    def _create_mpath_long_slug(self):
        if isinstance(self, Channel):
            if self.parent and self.parent != self:
                self.long_slug = "/".join([self.parent.long_slug, self.slug])
                self.mpath = "".join([self.parent.mapth, self.slug, ','])
            else:
                self.long_slug = self.slug
                self.mpaht = ",%s," % self.slug
        elif isinstance(self, Content):
                self.long_slug = "/".join([self.channel.long_slug, self.slug])
                self.mpath = "".join([self.channel.mpath, self.slug, ','])

    def validate_long_slug(self):
        self.create_mpath_long_slug()









class ChannelType(db.Model):
    pass


class Channel(db.model):
    pass
class Content(db.model):
    pass
