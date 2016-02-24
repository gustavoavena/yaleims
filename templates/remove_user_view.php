<div class="section">
    <div class="container">
        <div class="row">
            <div class="col-md-12">
                <h1 class="text-center">Remove User</h1>
                <p align="center">Click on the username to remove the user</p>
            </div>
        </div>
    </div>
</div>

<div class="section">
    <div class="container">
        <div class="row">
            <div class="col-md-12">
                <table class="table table-bordered table-condensed table-hover">
                    <thead>
                        <tr>
                            <th style="text-align:center">Username</th>
                            <th style="text-align:center">Full name</th>
                        </tr>
                    </thead>

                    <tbody id="tablebody" align="center">

                    <!--print the college's shields in a table in decrescent order according to their total points-->
                    <?php
                    foreach($users as $row)
                    {
                            print("<tr><td><a onclick=\"return userCheck(this);\"href=remove_user.php?user_id=" . $row["id"] . ">" . $row["username"] . "</a></td><td>" . $row["name"] . "</td></tr>");
                        
                    }
                    ?>
                    </tbody>

                </table>
            </div>
        </div>
    </div>
</div>
