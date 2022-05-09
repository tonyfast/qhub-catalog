import os
from contextlib import contextmanager

from dask_gateway import Gateway
from distributed import Client


@contextmanager
def dask_cluster(n_workers=2, worker_type="Small Worker", conda_env="filesystem/qhub_catalog"):
    try:
        gateway = Gateway()
        options = gateway.cluster_options()
        options.conda_environment = conda_env
        options.profile = worker_type
        print(f"Gateway: {gateway}")
        for key, value in options.items():
            print(f"{key} : {value}")

        cluster = gateway.new_cluster(options)
        client = Client(cluster)
        if os.getenv("JUPYTERHUB_SERVICE_PREFIX"):
            print(f"dask dashboard link: {cluster.dashboard_link}")

        cluster.scale(n_workers)
        client.wait_for_workers(1)

        yield client

    finally:
        cluster.close()
        client.close()
        del client
        del cluster