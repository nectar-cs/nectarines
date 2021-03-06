from prom_kaml.tests import prom_test_helper as my_helper
from kama_sdk.tests.t_helpers.cluster_test import ClusterTest
from prom_kaml.main.prom_data_supplier import PromDataSupplier
from prom_kaml.main import prom_data_supplier as supplier_module


class TestPromDataSupplier(ClusterTest):

  def test_resolve_default_client_config(self):
    if my_helper.easy_setup():
      supplier = PromDataSupplier.inflate({
        supplier_module.TYPE_KEY: 'vector'
      })
      self.assertTrue(supplier.resolve())

  def test_resolve_custom_client_config(self):
    if my_helper.easy_setup():
      supplier = PromDataSupplier.inflate({
        supplier_module.TYPE_KEY: 'ping',
        supplier_module.CLIENT_CONFIG: {}
      })
      self.assertTrue(supplier.resolve())

  def test_foo(self):
    thing = PromDataSupplier.inflate({
      'kind': PromDataSupplier.__name__,
      supplier_module.TYPE_KEY: 'vector',
      supplier_module.STEP_KEY: '15m',
      'source': group_query
    })
    result = thing.resolve()
    print(result)

  def test_supply_matrix(self):
    if my_helper.easy_setup():
      supplier = my_helper.vanilla_matrix_supplier()
      result = supplier.resolve()
      self.assertIsNotNone(result)
      self.assertGreater(len(result), 15)
      self.assertGreater(len(result[0].items()), 1)


group_query = "sum(" \
                "container_memory_usage_bytes{" \
                " container_name!='POD', " \
                " image!=''" \
                "}" \
              ") by(namespace)"
