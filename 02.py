<!DOCTYPE HTML>
<html lang="zh-cn">

<head>
    <meta charset="utf-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta content="width=device-width,initial-scale=1.0" name="viewport">
    <meta content="yes" name="apple-mobile-web-app-capable">
    <meta content="black" name="apple-mobile-web-app-status-bar-style">
    <meta content="telephone=no" name="format-detection">
    <meta content="email=no" name="format-detection">
    <title>系统管理</title>
    <link href="https://cdn.bootcss.com/bootstrap/3.3.7/css/bootstrap.min.css" rel="stylesheet">
    <link href="https://cdn.bootcss.com/bootstrap-table/1.11.1/bootstrap-table.min.css" rel="stylesheet">
    <link rel="stylesheet" href="https://cdn.bootcss.com/jquery-treegrid/0.2.0/css/jquery.treegrid.min.css">
    <style>
        .folder {
            font-weight: bold;
            color: #007bff; /* 目录名颜色 */
        }
    </style>
</head>

<body>
    <div class="container">
        <h1>树形表格 ： Table Treegrid</h1>
        <table id="table" class="table"></table>
        <br />
    </div>

    <script src="https://cdn.bootcss.com/jquery/3.1.1/jquery.min.js"></script>
    <script src="https://cdn.bootcss.com/bootstrap-table/1.12.1/bootstrap-table.min.js"></script>
    <script src="https://cdn.bootcss.com/bootstrap-table/1.12.0/extensions/treegrid/bootstrap-table-treegrid.js"></script>
    <script src="https://cdn.bootcss.com/jquery-treegrid/0.2.0/js/jquery.treegrid.min.js"></script>
    <script type="text/javascript">
        $(function () {
            var data = [
                // 这里填入从 Python 脚本生成的 JSON 数据
                {
                    "time": "2019-08-27",
                    "id": 1,
                    "content": "内容1",
                    "pid": ""
                }, {
                    "time": "2019-08-27",
                    "id": 2,
                    "content": "内容2",
                    "pid": 1
                }, {
                    "time": "2019-08-27",
                    "id": 3,
                    "content": "内容3",
                    "pid": 1
                }, {
                    "time": "2019-08-27",
                    "id": 4,
                    "content": "内容4",
                    "pid": ""
                }, {
                    "time": "2019-08-27",
                    "id": 5,
                    "content": "内容5",
                    "pid": 2
                },
                {
                    "time": "2019-08-27",
                    "id": 6,
                    "content": "内容6",
                    "pid": ""
                },
                {
                    "time": "2019-08-27",
                    "id": 7,
                    "content": "内容7",
                    "pid": 6
                },
            ];

            $('#table').bootstrapTable({
                data: data,
                idField: 'id',
                columns: [{
                    field: 'time',
                    title: '时间',
                    width: 140
                }, {
                    field: 'content',
                    title: '主要内容'
                }],
                treeShowField: 'time',
                parentIdField: 'pid',
                onResetView: function () {
                    $('#table').treegrid({
                        initialState: 'collapsed',
                        treeColumn: 0,
                        onChange: function () {
                            $('#table').bootstrapTable('resetWidth');
                        }
                    });
                },
            });
        });
    </script>
</body>
</html>
