$(function(){

//최초 실행되는 부분--------------------------------------------------------------------------
    let no = [1,2,3,4,5,6,7,8,9,10];
    let name = ['홍길동','유관순','이순신','김구','강감찬','김유신','홍길순','홍길자','최현묵','이규원'];
    let kor = [62,90,64,76,51,89,77,55,73,53];
    let eng = [70,62,73,54,55,60,67,77,51,100];
    let math = [81,79,50,83,72,79,82,86,50,94];
    let total = [213,231,187,213,178,228,226,218,174,247];
    let avg = [71,77,62.3,71,59.3,76,75.3,72.7,58,82.3];

    //tbody부문 10개 행 생성
    let htmlData = ""; //빈공간 초기화
    for(i=0; i<no.length; i++){
        htmlData += "<tr id='"+no[i]+"'>";
        htmlData += "<td><input type='checkbox' name='stu' class='stuChk' value='"+no[i]+"'></td>";
        htmlData += "<td>"+no[i]+"</td>";
        htmlData += "<td>"+name[i]+"</td>";
        htmlData += "<td>"+kor[i]+"</td>";
        htmlData += "<td>"+eng[i]+"</td>";
        htmlData += "<td>"+math[i]+"</td>";
        htmlData += "<td>"+total[i]+"</td>";
        htmlData += "<td>"+avg[i]+"</td>";
        htmlData += "<td>0</td>";
        htmlData += "<td><button class='delBtn'>삭제</button></td>";
        htmlData += "</tr>";        
    }//for

    //html소스를 id='tbody'에 추가
    $("#body").html(htmlData);

//최초 실행되는 부분 -----------------------------------------------------------------------

    //학생입력확인버튼
    $("#confirmBtn").click(function(){
        console.log("이름: "+$("#name").val());
        console.log("국어: "+$("#kor").val());
        console.log("영어: "+$("#eng").val());
        console.log("수학: "+$("#math").val()); //입력이 잘 되는지 확인

        let i_no = Math.max.apply(null.no)+1;
        let i_name = $("#name").val();
        let i_kor = $("#kor").val();
        let i_eng = $("#eng").val();
        let i_math = $("#math").val();
        let i_total = i_kor+i_eng+i_math;
        let i_avg = (i_total/3).toFixed(2);

        let htmlData = ""; //빈공간 초기화
            htmlData += "<tr id='"+i_no+"'>";
            htmlData += "<td><input type='checkbox' name='stu' class='stuChk' value='"+i_no+"'></td>";
            htmlData += "<td>"+i_no+"</td>";
            htmlData += "<td>"+i_name+"</td>";
            htmlData += "<td>"+i_kor+"</td>";
            htmlData += "<td>"+i_eng+"</td>";
            htmlData += "<td>"+i_math+"</td>";
            htmlData += "<td>"+i_total+"</td>";
            htmlData += "<td>"+i_avg+"</td>";
            htmlData += "<td>0</td>";
            htmlData += "<td><button class='delBtn'>삭제</button></td>";
            htmlData += "</tr>";    

        //html소스를 tbody에 추가
        $("#tbody").html(htmlData);

    })//학생입력확인버튼

        //전체 체크박스 선택(checked)
        $("#allChk").click(function(){ //좌상단 체크박스를 클릭했을 때
            if($(this).is(":checked")==true){  //모두 체크가 되었다면
                $(".stuChk").each(function(){ //each, 배열만큼 복사해서
                    $(this).prop("checked",true); //stuChk의 each만큼 체크를 true(on)
                })//전체 체크박스 선택
            }else{
                //전체 체크박스 해제
                $(".stuChk").each(function(){ //each, 배열만큼 복사해서
                    $(this).prop("checked",false); //stuChk의 each만큼 체크를 false(off)
                })//전체 체크박스 해제
            }//else
        })//좌상단 체크박스 클릭시

        //table에 있는 삭제버튼
        $(".delBtn").click(function(){
            console.log("1");
            console.log("현재 선택된 id: "+$(this).parent().parent().attr("id")); //attr(): ()의 속성값을 가져온다
            if(confirm("삭제하시겠습니까?")){
                $("#"+$(this).parent().parent().attr("id")).remove();
            }
        });//table 삭제

        //하단 삭제버튼 클릭
        $("#deletBtn").click(function(){
            console.log("체크박스 갯수: "+$(".stuChk").length);
            console.log("체크된 박스 갯수: "+$(".stuChk:checked").length);

            //체크되어 있는 것이 없을 경우
            if($(".stuChk:checked").length<1){
                alert("삭제 할 데이터를 체크하세요");
                return false;
            }
            //현재 박스가 체크되어있는지 확인
            if(!confirm("정말 삭제하시겠습니까?")){
                return false;
            }
            //모든 체크박스를 가져오기
            $(".stuChk").each(function(){
                if($(this).is(":checked")==true){
                    
                }
            })
        })

    

    
    
    
    
    
    
    
    
    


})//제이쿼리