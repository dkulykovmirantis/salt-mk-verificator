def test_galera_cluster_status(local_salt_client):
    gs = local_salt_client.cmd(
        'sql-*',
        'cmd.run',
        ['salt-call mysql.status | grep -A1 wsrep_cluster_size | tail -n1'])

    size_cluster = []
    amount = len(gs)

    for item in gs.values():
        size_cluster.append(item.split('\n')[-1].strip())

    assert size_cluster == ['{}'.format(amount)] * amount, \
        '''There found inconsistency within cloud. MySQL galera cluster
              is probably broken, the cluster size gathered from nodes:
              {}'''.format(gs)
