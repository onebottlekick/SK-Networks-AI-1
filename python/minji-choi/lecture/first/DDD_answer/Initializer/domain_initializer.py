from dice.repository.dice_repository_impl import DiceRepositoryImpl
from Player.repository.player_repository_impl import PlayerRepositoryImpl
class DomainInitializer:
    # @가 붙어있는 메소드들은 객체 생성 없이 사용할 수 있는 함수이다.

    @staticmethod
    def initDiceDomain():
        # 이 부분에서 기존에 만들어진 것을 받아옴
        # 만약 기존에 만들어진 것이 없다면 새로 만들고
        # 이후 요청되는 것들은 기존에 만들어진 것을 반환함(싱글톤 특성)

        DiceRepositoryImpl.getInstance()

    @staticmethod
    def initPlayerDomain():
        PlayerRepositoryImpl.getInstance()


    @staticmethod
    def initEachDomain():
        DomainInitializer.initDiceDomain()
        DomainInitializer.initPlayerDomain()