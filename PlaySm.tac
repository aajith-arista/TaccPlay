<<= TacModule("Play");

PlayNs : Tac::Namespace {

MemberSm : Tac::Type( member ) : Tac::Constrainer {
   member : PlayMember::PtrConst;
   name : : member::name;

   handleDel : extern invasive void();
   handleInitialized : extern invasive void();

   this => {
      `isAppliedInDestructor;
      handleDel();
   }

   initialized : bool;
   initialized => initially handleInitialized();
}

PlaySm :  Tac::Type( play ) : Tac::Constrainer {
   `hasFactoryFunction;
   play : in Play::PtrConst;

   memberSm : MemberSm[name];

   handleMember : extern invasive void ( name : Tac::String );
   play::member[name] => handleMember(name);

   initialized : bool;
   handleInitialized : extern invasive void();
   initialized => initially handleInitialized();
}

}
<<= CppBlock( "PlaySm.tin" );
