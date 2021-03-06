import os

from kama_sdk import entrypoint
from kama_sdk.model.base.model import models_man
from kama_sdk.core.core import utils, kaml_man
from lib.consts import IceCreamConsts
from lib.website_helper import WebsiteHelper


def register_self():
  root_dir = os.path.dirname(os.path.abspath(__file__))
  yamls = utils.yamls_in_dir(f'{root_dir}/configs', recursive=True)
  models_man.add_app_descriptors(yamls)
  models_man.add_classes([
    IceCreamConsts,
    WebsiteHelper
  ])


def register_libraries():
  kaml_man.register_kaml('telem_kaml')
  kaml_man.register_kaml('prom_kaml')


if __name__ == '__main__':
  register_libraries()
  register_self()
  entrypoint.start()
