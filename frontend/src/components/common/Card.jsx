function Card({ children }) {
    return (
      <div
        className="
          w-full
          rounded-3xl
          border border-white/30
          bg-white/60
          p-8
          shadow-2xl
          backdrop-blur-xl
        "
      >
        {children}
      </div>
    );
  }
  
  export default Card;