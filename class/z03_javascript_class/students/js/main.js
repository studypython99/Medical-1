//  1. ajax stu_score.json 10개 데이터를 출력하시오.
$(function(){

//전역변수
let s_count = 1; //학생번호
let o_id = 0;
let o_no = 0;
let o_name = "";
let o_kor = 0;
let o_eng = 0;
let o_math = 0;


    $.ajax({
        url:"./json/stu_score.json",
        data:"",
        type:"get",
        dataType:"json",
        success:function(data){
            alert("ajax success :D");
            console.log(data);

            let htmlData = "";
            for(i=0; i<10; i++){
                htmlData += "<tr id='"+data[i].no+"'>";
                htmlData += "<td><input type='checkbox' name='stu' class='stuChk' value='"+data[i].no+"'체크박스</td>";
                htmlData += "<td>"+data[i].no+"</td>";
                htmlData += "<td>"+data[i].name+"</td>";
                htmlData += "<td>"+data[i].kor+"</td>";
                htmlData += "<td>"+data[i].eng+"</td>";
                htmlData += "<td>"+data[i].math+"</td>";
                htmlData += "<td>"+data[i].total+"</td>";
                htmlData += "<td>"+data[i].avg+"</td>";
                htmlData += "<td>"+data[i].rank+"</td>";
                htmlData += "<td><button class='delBtn'>삭제</button></td>";
                htmlData += "</tr>";
                s_count++; //번호를 하나씩 증가시켜서 받는다 
            }//for
            $("#body").html(htmlData);
        },//success
        error:function(){
            alert("ajax error :(");
        }//error

    });//ajax


//  2. 학생입력 > 학생추가 프로그램을 구성하시오

//학생입력버튼을 누르면
$("#writeBtn").click(function(){
    alert("click writeBtn")

    //학생입력하는 창이 뜨고
    //.p_all의 css를 display none > display block 으로 변경
    $(".p_all").css("display","block");
    //.p_main의 text 문구를 "학생성적입력" 으로 변경
    $(".p_main h2").text("학생성적입력");
    //id="name"의 readonly를 false로 변경, prop사용
    $("#name").prop("readonly",false);

})
    //학생입력>취소
    //취소버튼을 누르면
    $("#cancelBtn").click(function(){
        //.p_all의 css를 display block > display none 으로 변경
        $(".p_all").css("display","none");
        //초기화 한다. #id,name,kor,eng,math.val("");
        $("#id").val("");
        $("#name").val("");
        $("#kor").val("");
        $("#eng").val("");
        $("#math").val("");
    })//cancelBtn
    //학생입력>확인
    //확인버튼을 누르면
    $("#confirmBtn").click(function(){
        //새로운 학생을 입력한다
        let i_no = s_count + 1;
        let i_name = $("#name").val();
        let i_kor = Number($("#kor").val());
        let i_eng = Number($("#eng").val());
        let i_math = Number($("#math").val());
        let i_total = i_kor + i_eng + i_math;
        let i_avg = (i_total/3).toFixed(2)

        //table tr 위치에 추가시킨다
        let htmlData = "";
        htmlData += "<tr id='"+s_count+"'>";
        htmlData += "<td><input type='checkbox' name='stu' class='stuChk' value='"+i_no+"'체크박스</td>";
        htmlData += "<td>"+s_count+"</td>";
        htmlData += "<td>"+i_name+"</td>";
        htmlData += "<td>"+i_kor+"</td>";
        htmlData += "<td>"+i_eng+"</td>";
        htmlData += "<td>"+i_math+"</td>";
        htmlData += "<td>"+i_total+"</td>";
        htmlData += "<td>"+i_avg+"</td>";
        htmlData += "<td>0</td>";
        htmlData += "<td><button class='delBtn'>삭제</button></td>";
        htmlData += "</tr>";
        s_count++ //초기에 증가시킨 데이터 다음으로 하나씩 증가시킨다
        //html소스를 tbody에 추가, append로 화면 마지막줄에 입력된다
        $("#body").append(htmlData);
        //추가 후 input내용을 초기화한다
        $("#name").val(""); //val("") << 공백으로 만듦
        $("#kor").val("");
        $("#eng").val("");
        $("#math").val("");
    })//confirmBtn

//  3. 학생수정 > 학생성적수정이 가능하게 구성하시오
$("#modifyBtn").click(function(){
    alert("click modifyBtn")

    //학생입력하는 창이 뜨고
    //.p_all의 css를 display none > display block 으로 변경
    $(".p_all").css("display","block");
    //.p_main의 text 문구를 "학생성적수정" 으로 변경
    $(".p_main h2").text("학생성적수정");
    //id="name"의 readonly를 false로 변경, prop사용
    $("#name").prop("readonly",false);
})
//수정버튼을 누르면
//이름 국 영 수 를 입력받아서
//해당 id번호 위치에 입력한다.

//  4. 학생삭제 > 선택된 학생이 삭제되도록 구성하시오


});//jquery