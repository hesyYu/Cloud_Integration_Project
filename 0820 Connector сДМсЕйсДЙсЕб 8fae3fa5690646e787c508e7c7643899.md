# 0820 Connector 조사

- w[ebMethods.io](http://webmethods.io) Integration Connector
    - Twitter
        - Twitter 란?

            ![image/Untitled.png](image/test.png)

            Twitter는 실시간 업데이트를 제공하는 전 세계와 연결되는 소셜 네트워크. 

            이를 통해 트윗을 게시하고, 개인 메시지를 통해 상호 작용하고, 유명인과 사고 리더를 팔로우하고, 글로벌 커뮤니케이션에 참여할 수 있다.

        - Triggers
            - User Tweet or Mention: 지정된 해시 태그, 사용자 트윗 또는 언급 된 사용자에 대해 트리거된다.
            - Direct Message Sent: 계정에서 쪽지가 전송 될 때 트리거된다.
            - Direct Message Received: 계정에서 쪽지가 수신 될 때 트리거된다.
            - New Tweet or Retweet Posted by Me: 계정에서 새 트윗 또는 리트 윗이 게시 될 때 트리거된다.
            - Tweet Mentioning You: 계정에서 언급 된 트윗을받을 때 트리거된다.
            - New Follower: 사용자가 현재 로그인 한 사용자를 팔로우 할 때 트리거된다.
            - Liked Tweet: 누군가 내 트윗을 좋아할 때 트리거된다.
            - New Tweet in Timeline: 팔로우하는 계정에서 새 트윗이 게시 될 때 트리거된다.

        - Action
            - Search Tweets: 특정 키워드로 최신 트윗 검색 및 검색
            - Post Tweet: 새 트윗 게시
            - Retweet: 특정 트윗을 리트윗
            - Upload Image: 지정된 이미지를 업로드

    - Google Drive
        - Google Drive 란?

            ![image/test201.png](image/test201.png)

            Google 드라이브는 모든 파일을 저장하고 동료와 공유하는 클라우드 기반 스토리지 플랫폼. 

            모든 데이터를 동기화하고 모든 장치에서 액세스 할 수 있다.

        - Triggers
            - File or Folder Created: 기존 파일 또는 폴더가 생성 될 때 트리거된다.
            - Comment in File: 파일에 새 주석이 추가 될 때 트리거된다.
            - File Updated: 기존 파일이 업데이트 될 때 트리거된다.

        - Actions
            - Copy File: 파일 사본을 만들고 패치 시맨틱으로 요청 된 업데이트를 적용한다.
            - Create Comment: 파일에 대한 새 댓글 작성
            - Create Permission: 파일에 대한 권한 생성
            - Create Reply: 댓글에 대한 새 답글 작성
            - Delete Comment By ID: ID를 전달하여 댓글을 삭제
            - Delete File By ID: 사용자가 소유 한 아이디로 파일을 휴지통으로 옮기지 않고 영구 삭제
            - Delete Permission By ID: ID 별 권한 삭제
            - Delete Reply By ID: 아이디로 답장을 삭제한다.
            - Delete Revision By ID: ID로 파일 수정본을 삭제한다.
            - Download File By ID: Google 드라이브에 저장된 ID로 파일을 다운로드한다.
            - Empty Trash: 사용자가 소유 한 파일을 휴지통으로 이동하지 않고 영구적으로 삭제한다.
            - Export File: Google 문서를 요청 된 MIME 유형으로 내보내고 내 보낸 콘텐츠를 반환한다.
            - Generate File IDs: 생성 요청에서 제공 할 수있는 파일 ID 세트를 생성한다.
            - Get Comment By ID: ID로 댓글 받기
            - Get File By ID: 파일의 메타 데이터 또는 ID로 지정된 콘텐츠를 반환한다.
            - Get Permission By ID: ID로 권한 받기
            - Get Reply By ID: 아이디로 답장 받기
            - Get Resumable Session: 재개 가능한 세션 URI를 반환한다.
            - Get Revision By ID: ID로 개정판의 메타 데이터 또는 콘텐츠를 가져온다.
            - Get Start Page Token: 향후 변경 사항을 나열하기 위해 시작 페이지 토큰을 가져온다.
            - Get User Information: 사용자, 사용자 드라이브 및 시스템 기능에 대한 정보를 가져온다.
            - List Changes: 사용자에 대한 목록 변경
            - List Comments: 파일의 주석 나열
            - List Files: 파일 나열 또는 검색
            - List Permissions: ID별로 권한 나열
            - List Replies: 댓글의 답글 나열
            - List Revisions: 파일의 개정판 나열
            - Simple Upload File: Google 드라이브에 단순 업로드를 수행 할 수 있다.
            - Update Comment: 파일의 메타 데이터 또는 콘텐츠를 ID로 반환
            - Update Metadata For File: 파일의 메타 데이터를 업데이트한다.
            - Update Permission: 파일에 대한 권한 업데이트
            - Update Reply: 패치 시맨틱으로 응답 업데이트
            - Update Revision: 파일의 개정판을 업데이트한다.
            - Upload File: Google 드라이브에 재개 가능한 업로드를 수행 할 수 있다.

    - Google Maps
        - Google Maps 란?

            ![image/test202.png](image/test202.png)

            Google지도는 정확하고 신뢰할 수있는 위치 정보를 실시간으로 제공하는 웹 매핑 서비스로 쉽고 간편한 탐색을 지원합니다.

        - Actions
            - Get Direction : 어느 장소 나 위치에 도달 할 방향을 검색합니다.
            - Get Distance Matrix : 출발지 및 목적지 매트릭스에 대한 이동 거리 및 시간을 검색합니다.

    - Marketo
        - Marketo 란?

            ![image/test203.png](image/test203.png)

            Marketo는 기업이 기존 및 잠재 고객과 소통 할 수 있도록 클라우드 기반 마케팅 자동화 소프트웨어를 제공한다.

            리드에 대한 레코드를 생성 및 유지하고, 기회를 식별하고, 조직을위한 이메일 템플릿을 생성 할 수 있다.

        - Triggers
            - New Lead: 새 리드가 생성 될 때 트리거된다.
            - New Lead in List: 지정된 목록에 새 리드가 생성 될 때 트리거된다.
            - Update Lead: 기존 리드가 업데이트 될 때 트리거된다.
            - Update Lead in List: 지정된 목록에서 기존 리드가 업데이트 될 때 트리거된다.
            - New List: 새 목록이 생성 될 때 트리거된다.
            - New Campaign: 새 캠페인이 생성 될 때 트리거된다.

        - Actions
            - addLeadsToList : 목록에 리드 추가
            - createCompanies : 하나 이상의 회사 만들기
            - createOpportunities : 하나 이상의 기회 생성
            - createOpportunityRoles : 새 기회 역할 만들기
            - createSalesPersons : 새 영업 사원 생성
            - deleteCompanyByDedupeFields : 지정된 회사 중복 제거 필드 또는 ID 필드를 삭제
            - deleteCompanyByIDFields : 중복 제거 필드 또는 ID 필드를 사용하여 특정 회사를 삭제
            - deleteLeads : 지정된 리드 개체 삭제
            - deleteOpportunityByDedupeFields : 중복 제거 필드를 사용하여 특정 기회 삭제
            - deleteOpportunityByIDFields : ID를 사용하여 특정 기회 삭제
            - deleteOpportunityRoleByDedupeField : 중복 제거 ID를 사용하여 특정 기회 역할 삭제
            - deleteOpportunityRoleByIDFields : ID를 사용하여 특정 기회 역할 삭제
            - deleteSalesPersonByDedupeField : 중복 제거 ID를 사용하여 지정된 영업 사원을 삭제
            - deleteSalesPersonByIDFields : ID를 사용하여 특정 영업 사원 삭제
            - getActivityTypes : Marketo에서 사용할 수있는 활동 유형에 대한 메타 데이터 반환
            - getCampaignById : marketo에서 사용할 수있는 캠페인 검색
            - getChannels : 채널 목록 검색
            - getDeletedLeads : 삭제 된 리드 목록을 반환
            - getLeadActivities : 요청 된 활동 유형에 대한 리드 검색
            - getLeadById : 지정된 ID를 가진 리드를 검색
            - getLeadPartition : 특정 파티션의 세부 정보를 반환
            - getMarketoLeadChangesActivities : 활동에 대한 리드 변경 목록 가져 오기
            - getMarketoLeadChangesActivityInChunks : 청크의 리드 변경 목록 가져 오기
            - getMultipleLists : 여러 목록 검색
            - getNewLeadActivities : 새 리드 활동 목록 검색
            - getPagingToken : 주어진 날짜에 대한 토큰 반환
            - getTags : 대상 인스턴스에서 사용 가능한 모든 태그 목록을 반환
            - isLeadMemberOfList : 리드가 지정된 목록의 구성원인지 확인
            - mergeLead : 두 리드 병합
            - queryCompanies : 지정된 입력 매개 변수를 사용하여 회사 정보 검색
            - queryLeadbyListId : 지정된 리드의 세부 사항을 검색
            - queryLeadbyProgramId : 주어진 프로그램 ID에서 여러 리드 검색
            - queryLeads : 주어진 검색 기준에 대해 여러 리드를 검색
            - queryOpportunities : 주어진 검색 기준에 대해 여러 기회를 검색
            - queryOpportunityRoles : 지정된 검색 기준에 대해 여러 기회 역할을 검색
            - querySalesPersons : 주어진 검색 기준에 대해 여러 영업 사원을 검색
            - removeLeadsFromList : 목록에서 리드 제거, 정적 목록 만 API를 통해 액세스 할 수 있다. 스마트 목록에 액세스 할 수 없다.
            - requestCampaign : Marketo 스마트 캠페인에서 기존 Marketo 리드 실행
            - scheduleCampaign : 캠페인 예약
            - updateCompaniesbyDedupeFields : 중복 제거 필드를 사용하여 특정 회사 업데이트
            - updateOpportunitiesbyDedupeFields : 중복 제거 필드를 사용하여 특정 기회 업데이트
            - updateOpportunitiesbyID : ID를 사용하여 특정 기회 업데이트
            - updateOpportunityRolesbyDedupeFields : 중복 제거 필드를 사용하여 특정 기회 역할 업데이트
            - updateOpportunityRolesbyID : ID를 사용하여 특정 기회 업데이트
            - updateSalesPersonsbyDedupeFields : 중복 제거 필드를 사용하여 특정 영업 사원 레코드를 업데이트
            - updateSalesPersonsbyID : ID를 사용하여 특정 기회 업데이트
            - upsertCompanies : 지정된 회사에 대한 Upsert 데이터
            - upsertLeads : 데이터 특정 리드를 Upsert
            - upsertOpportunities : 특정 기회에 대한 Upsert 데이터
            - upsertOpportunityRoles : 특정 기회 역할에 대한 Upsert 데이터
            - upsertSalesPersons : 영업 사원에 대한 Upsert 데이터
    - Firebase
        - Firebase 란?

            ![image/test204.png](image/test204.png)

            Firebase는 클라이언트 측과 서버 측 모두에서 데이터를 동기화하고 저장하는 확장 가능한 클라우드 기반 NoSQL 데이터베이스입니다.

            클라우드 플랫폼 통합을 사용하여 모바일, 웹, 서버 환경을위한 유연한 개발을 제공합니다.

        - Actions
            - Firestore Update Record : 지정된 프로젝트의 레코드를 업데이트