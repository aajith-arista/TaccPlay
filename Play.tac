taccExtension << "attrLog";

PlayNs : Tac::Namespace {

PlayMember : Tac::Type( name ) : Tac::Entity {
   name : Tac::String;
   val : U32;
}

Play : Tac::Type() : Tac::Entity {
   `hasFactoryFunction;
   pa1 : U32;
   member : PlayMember[ name ];
}

}
