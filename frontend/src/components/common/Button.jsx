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
          bg-slate-900
          px-6
          py-3.5
          text-base
          font-semibold
          text-white
          shadow-lg
          transition-all
          duration-200
          hover:-translate-y-0.5
          hover:bg-orange-400
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