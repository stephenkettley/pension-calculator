function Button({
    children,
    type = "button",
    ...props
  }) {
    return (
      <button
        type={type}
        className="
          w-full
          rounded-xl
          px-6
          py-3.5
          text-base
          font-semibold
          text-white
          shadow-lg
          transition-all
          duration-200
          bg-sky-900
          hover:bg-slate-900
          hover:-translate-y-0.5
          hover:shadow-xl
          active:translate-y-0
          disabled:cursor-not-allowed
          disabled:opacity-50
        "
        {...props}
   
   
   
      >
        {children}
      </button>
    );
  }
  
  export default Button;