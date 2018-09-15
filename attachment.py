# This file is part of the pyme module for Tryton.
# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
import os
from trytond.config import config as config_
from trytond.pool import PoolMeta
from trytond.transaction import Transaction

__all__ = ['Attachment']


class Attachment(metaclass=PoolMeta):
    __name__ = 'ir.attachment'

    @classmethod
    def delete(cls, attachments):
        cursor = Transaction().connection.cursor()
        db_name = cursor.dbname
        base_path = os.path.join(config_.get('database', 'path'), db_name)
        archives = []
        for attachment in attachments:
            archive = attachment.digest
            if not archive:
                continue
            collision = attachment.collision
            directory = os.path.join(base_path, archive[0:2], archive[2:4])
            if collision:
                archive += '-' + str(collision)
            archives.append('%s/%s' % (directory, archive))

        super(Attachment, cls).delete(attachments)

        for archive in archives:
            if os.path.isfile(archive):
                os.unlink(archive)
                try:
                    directories = ('/'.join(archive.split('/')[0:-1]),
                        '/'.join(archive.split('/')[0:-2]))
                    map(os.rmdir, directories)
                except OSError:
                    pass
