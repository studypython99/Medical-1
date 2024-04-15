$(function(){
  //최초 실행되는 부분
    let no = [1,2,3,4,5,6,7,8,9,10];
    let name = ['홍길동','유관순','이순신','김구','강감찬','김유신','홍길순','홍길자','최현묵','이규원'];
    let kor = [62,90,64,76,51,89,77,55,73,53];
    let eng = [70,62,73,54,55,60,67,77,51,100];
    let math = [81,79,50,83,72,79,82,86,50,94];
    let total = [213,231,187,213,178,228,226,218,174,247];
    let avg = [71,77,62.3,71,59.3,76,75.3,72.7,58,82.3];
    
    //tbody부문 10개 행 생성
    let htmlData = "";
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
    
    //html소스를 tbody에 추가
    $("#body").html(htmlData);

  //최초 실행되는 부분------------------------------

    // 학생성적 입력창이 팝업으로 뜨도록
    $("#writeBtn").click(function(){
        alert("writebtn test")
        $(".p_all").css("display","block");
    });//학생성적 입력창
    
    //학생성적 입력창 닫기
    $("#cancelBtn").click(function(){
        alert("writebtn test")
        $(".p_all").css("display","none");
    });//학생성적 입력창 닫기

    //학생입력확인버튼
    $("#confirmBtn").click(function(){
        //글자text(), input val(), html()
        //console.log("이름: "+$("#name").val());
        //console.log("국어: "+$("#kor").val());
        //console.log("영어: "+$("#eng").val());
        //console.log("수학: "+$("#math").val());
        //console.log(Math.max.apply(null,no)+1); //this, 여기에 들어갈 값이 없기에 null표시
        //no.push(Math.max.apply(null,no)+1); //배열추가

        //공백확인, input창에 입력이 안되어있으면 alert이 뜬다
        if($("#name").val().length<2){ //글씨가 두글자 이하면,
            alert("이름을 입력하시오 (2글자 이상)")
            $("#name").focus();
            return false;
        }

        //번호생성은 DB에서 자동으로 부여됨,
        let i_no = Math.max.apply(null,no)+1
        no.push(i_no);
        let i_name = $("#name").val();
        let i_kor = Number($("#kor").val());
        let i_eng = Number($("#eng").val());
        let i_math = Number($("#math").val());
        let i_total = i_kor+i_eng+i_math;
        let i_avg =(i_total/3).toFixed(2); //소수점 2자리 반올림
        let i_rank = 0;

        // table tr추가하기(학생입력)
        let htmlData = "";
        htmlData += "<tr id='"+i_no+"'>";
        htmlData += "<td><input type='checkbox' name='stu' class='stuChk' value='"+i_no+"'></td>";
        htmlData += "<td>"+i_no+"</td>";
        htmlData += "<td>"+i_name+"</td>";
        htmlData += "<td>"+i_kor+"</td>";
        htmlData += "<td>"+i_eng+"</td>";
        htmlData += "<td>"+i_math+"</td>";
        htmlData += "<td>"+i_total+"</td>";
        htmlData += "<td>"+i_avg+"</td>";
        htmlData += "<td>"+i_rank+"</td>";
        htmlData += "<td><button class='delBtn'>삭제</button></td>";
        htmlData += "</tr>";     
    
    //html소스를 tbody에 추가, 기존 html을 덮어쓰기
    //$("#body").html(htmlData);
    //$("#body").parent(htmlData); //기존 html 위쪽에 추가
    $("#body").append(htmlData); //기존 html 뒤쪽에 추가

    //input초기화, 빈공백을 입력해라
    $("#name").val("");
    $("#kor").val("");
    $("#eng").val("");
    $("#math").val("");
    $(".p_all").css("display","none");
    
})//학생입력버튼

    //전체선택, 취소
    $("#allChk").click(function(){
        if($(this).is(":checked")==true){// 좌상단 체크박스 클릭시
            //모두 체크
            console.log("체크됨")
            //each, 배열만큼 반복
            $(".stuChk").each(function(){
                $(this).prop("checked",true); //.stuChk의 each만큼 체크를 true(on) 
            })
        }else{
            //모두 체크 해제
            console.log("체크해제")
            $(".stuChk").each(function(){
                $(this).prop("checked",false); //.stuChk의 each만큼 체크를 false(off) 
            })
        }//else

    });//좌상단 체크박스 클릭시

    //table에 있는 삭제버튼, document에서 .delBtn을 다시 찾아야한다. 추가등록이 삭제 안되는 경우;;
    $(document).on("click",".delBtn",function(){
        console.log($(this).parent().parent().attr("id"));
        if(confirm("정말 삭제하시겠습니까?")){
            $("#"+$(this).parent().parent().attr("id")).remove();
        }
    });

    /**
    $(".delBtn").click(function(){
        console.log("1")
        console.log("현재 선택된id: "+$(this).parent().parent().attr("id"));
        if(confirm("삭제하시겠습니까?")){
            $("#"+$(this).parent().parent().attr("id")).remove();
        }
    });//table 삭제 */
    
    //하단 삭제버튼 클릭
    $("#deletBtn").click(function(){
        //alert("test");
        console.log("체크박스 갯수: "+$(".stuChk").length);
        console.log("체크된 박스 갯수: "+$(".stuChk:checked").length);
        //console.log("체크된 박스 갯수: "+$("input:checkbox[name='stu']:checked").length);
        
        //체크되어 있는 것이 없을 경우
        if($(".stuChk:checked").length<1){
            alert("삭제할 데이터를 체크하세요");
            return false;
        }
        //현재 박스가 체크되어있는지 확인
        if(!confirm("정말 삭제하시겠습니까?")){
            return false; //no버튼 클릭시 다시 돌아감, yes누를 시 패스
        }
        //모든 체크박스를 가져오기
        $(".stuChk").each(function(){

            //??? 왜 콘솔이 안뜰까? , 삭제를 눌러야 뜸 ㅎㅎ
            if($(this).is(":checked") ==true){
                console.log("현재 선택된class: "+$(this).val());
                console.log("현재 선택된idd: "+$(this).parent().parent().attr("id"));
                $("#"+$(this).parent().parent().attr("id")).remove();
            }
        });//each
    });//하단삭제버튼
    
});//제이쿼리
    
    
